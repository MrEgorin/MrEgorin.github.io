document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------
    // Burger menu functionality
    // ----------------------------------------------------
    const burgerMenu = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');

    if (burgerMenu && navLinks) {
        burgerMenu.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // ----------------------------------------------------
    // Page fade-out transition on navigation
    // ----------------------------------------------------
    const pageLinks = document.querySelectorAll('a.nav-button, a.nav-logo-link, a.pub-link');
    pageLinks.forEach(link => {
        const targetUrl = link.getAttribute('href');
        const targetAttr = link.getAttribute('target');
        
        // Only transition internal links, not external links or blank target tabs
        if (targetUrl && !targetUrl.startsWith('http') && targetAttr !== '_blank') {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                document.body.style.opacity = '0';
                
                // Smart Routing Patch:
                // If running locally via file:// protocol, append 'index.html' to directory paths 
                // so browser doesn't throw a directory index error.
                let destination = targetUrl;
                if (window.location.protocol === 'file:') {
                    if (destination === './' || destination === '../') {
                        destination += 'index.html';
                    } else if (destination.endsWith('/')) {
                        destination += 'index.html';
                    }
                }
                
                setTimeout(() => {
                    window.location.href = destination;
                }, 250);
            });
        }
    });

    // Fade-in effect on page load
    document.body.style.opacity = '1';

    // ----------------------------------------------------
    // Dynamic Molecular Canvas Background Animation
    // ----------------------------------------------------
    const canvas = document.createElement('canvas');
    canvas.id = 'molecule-canvas';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    
    let particles = [];
    const maxParticles = 60;
    const connectionDist = 120;
    let mouse = { x: null, y: null, radius: 150 };

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.radius = Math.random() * 2 + 1;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(0, 242, 254, 0.25)';
            ctx.fill();
        }

        update() {
            // Bounce off boundaries
            if (this.x < 0 || this.x > canvas.width) this.vx = -this.vx;
            if (this.y < 0 || this.y > canvas.height) this.vy = -this.vy;

            // Mouse interaction (gentle repulsion)
            if (mouse.x !== null && mouse.y !== null) {
                const dx = this.x - mouse.x;
                const dy = this.y - mouse.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < mouse.radius) {
                    const force = (mouse.radius - dist) / mouse.radius;
                    const angle = Math.atan2(dy, dx);
                    this.x += Math.cos(angle) * force * 1.5;
                    this.y += Math.sin(angle) * force * 1.5;
                }
            }

            this.x += this.vx;
            this.y += this.vy;
        }
    }

    // Initialize particles
    for (let i = 0; i < maxParticles; i++) {
        particles.push(new Particle());
    }

    // Track mouse
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    window.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });

    // Animation Loop
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
            
            // Draw connections between particles
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                
                if (dist < connectionDist) {
                    const alpha = (1 - dist / connectionDist) * 0.15;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(0, 242, 254, ${alpha})`;
                    ctx.lineWidth = 0.8;
                    ctx.stroke();
                }
            }
        }
        
        requestAnimationFrame(animate);
    }
    
    animate();
});
