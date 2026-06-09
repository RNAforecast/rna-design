/* ─────────────────────────────────────────────────────────
   RNA Design · main.js
   Vanilla JS, no dependencies.
───────────────────────────────────────────────────────── */

/* ── 1. Nav: scroll state ──────────────────────────────── */
const navEl = document.getElementById('nav');
if (navEl) {
    const onScroll = () => navEl.classList.toggle('scrolled', window.scrollY > 40);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
}

/* ── 2. Nav: mobile toggle ─────────────────────────────── */
const navToggle = document.getElementById('navToggle');
const navMenu   = document.getElementById('navLinks');
if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
        const nowOpen = navMenu.classList.toggle('open');
        navToggle.setAttribute('aria-expanded', String(nowOpen));
    });

    document.addEventListener('click', (e) => {
        if (navEl && !navEl.contains(e.target)) {
            navMenu.classList.remove('open');
            navToggle.setAttribute('aria-expanded', 'false');
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu.classList.contains('open')) {
            navMenu.classList.remove('open');
            navToggle.setAttribute('aria-expanded', 'false');
            navToggle.focus();
        }
    });
}

/* ── 3. Scroll reveal ──────────────────────────────────── */
const revealEls = document.querySelectorAll('.reveal');
if (revealEls.length) {
    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                const idx = parseInt(entry.target.dataset.revealIndex ?? '0', 10);
                setTimeout(() => entry.target.classList.add('visible'), idx * 80);
                revealObserver.unobserve(entry.target);
            });
        },
        { threshold: 0.12 }
    );
    revealEls.forEach((el, i) => {
        el.dataset.revealIndex = String(i);
        revealObserver.observe(el);
    });
}

/* ── 4. RNA path animation ─────────────────────────────── */
document.querySelectorAll('svg .rna-path').forEach((el) => {
    if (typeof el.getTotalLength !== 'function') return;
    const len = el.getTotalLength();
    el.style.strokeDasharray  = len;
    el.style.strokeDashoffset = len;
    el.style.transition = 'stroke-dashoffset 1.8s cubic-bezier(0.4, 0, 0.2, 1)';
    /* double rAF: initial offset is painted before transition fires */
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            el.style.strokeDashoffset = '0';
        });
    });
});

/* ── 5. Abstract toggle ────────────────────────────────── */
document.querySelectorAll('.abstract-toggle').forEach((btn) => {
    btn.addEventListener('click', () => {
        const body     = btn.nextElementSibling;
        if (!body || !body.classList.contains('abstract-body')) return;
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!expanded));
        body.hidden    = expanded;
        btn.textContent = expanded ? 'Show summary' : 'Hide summary';
    });
});

/* ── 6. Contact form (FormSubmit AJAX) ─────────────────── */
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const submitBtn = contactForm.querySelector('[type="submit"]');
        if (!submitBtn || submitBtn.disabled) return;

        if (!contactForm.checkValidity()) {
            contactForm.reportValidity();
            return;
        }

        submitBtn.disabled    = true;
        submitBtn.textContent = 'Sending…';

        const data = Object.fromEntries(new FormData(contactForm).entries());

        fetch(contactForm.action, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: JSON.stringify(data),
        })
        .then((res) => res.json())
        .then((res) => {
            if (res.success === 'true' || res.success === true) {
                submitBtn.textContent       = 'Message sent ✓';
                submitBtn.style.background  = 'transparent';
                submitBtn.style.borderColor = 'var(--teal)';
                submitBtn.style.color       = 'var(--teal)';
                contactForm.reset();
            } else {
                throw new Error('FormSubmit error');
            }
        })
        .catch(() => {
            submitBtn.disabled    = false;
            submitBtn.textContent = 'Send Message';
            alert('Something went wrong — please email directly at michael.wolfinger@univie.ac.at');
        });
    });
}

/* ── 7. Footer: current year ────────────────────────────── */
const yearEl = document.getElementById('footer-year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

/* ── 8. Hero bracket ticker ─────────────────────────────── */
const bracketStrip = document.querySelector('.hero__bracket-strip');
if (bracketStrip) {
    const pattern = '(((....))) (((...))) (((((..(((...)))..))))) ';
    bracketStrip.textContent = pattern.repeat(8);
}
