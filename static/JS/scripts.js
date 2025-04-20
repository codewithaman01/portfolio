document.addEventListener('DOMContentLoaded', function () {
    console.log("Document loaded");

    // Smooth scroll to sections
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Toggle theme
    const footer = document.querySelector('footer');
    footer.insertAdjacentHTML('beforeend', `
        <br><button id="darkModeToggle" class="btn btn-sm btn-secondary">Toggle Dark Mode</button>
    `);

    document.getElementById("darkModeToggle").addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
    });
});

document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    fetch('/submit-comment/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const commentSection = document.querySelector('.comments-section');
            const newComment = document.createElement('div');
            newComment.className = 'comment mb-4';
            newComment.innerHTML = `
                <p><strong>${data.name}</strong> (${data.created_at})</p>
                <p>${data.comment}</p>
            `;
            commentSection.prepend(newComment);
            form.reset();
        } else {
            alert("Something went wrong!");
        }
    })
    .catch(err => {
        console.error(err);
    });
});
