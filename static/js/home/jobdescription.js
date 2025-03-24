document.addEventListener("DOMContentLoaded", function () {
    let applyBtn = document.getElementById("applyBtn");

    if (applyBtn) {
        applyBtn.addEventListener("click", function(event) {
            event.preventDefault();  // Stop immediate redirection

            let jobId = this.getAttribute("data-job-id");  // Get Job ID
            let applyUrl = this.href;  // Store the external URL

            fetch(`/track-apply/${jobId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),  // Fetch CSRF token
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById("applicationCount").innerText = data.applications;  // Update UI count
                }
                window.location.href = applyUrl;  // Redirect after tracking
            })
            .catch(error => {
                console.error("Error tracking application:", error);
                window.location.href = applyUrl;  // Redirect even if tracking fails
            });
        });
    } else {
        console.error("applyBtn not found in the DOM.");
    }
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}