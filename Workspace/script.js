<script>
// Custom Script
    document.addEventListener("DOMContentLoaded", function () {

        // Copy button
        document.querySelectorAll("pre").forEach(pre => {
            if (!pre.querySelector(".copy-btn")) {
                let button = document.createElement("button");
                button.innerText = "Copy";
                button.classList.add("copy-btn");
                button.onclick = function () {
                    let codeText = pre.querySelector("code").innerText;
                    navigator.clipboard.writeText(codeText).then(() => {
                        button.innerText = "Copied";
                        button.classList.add("copied");

                        setTimeout(() => {
                            button.innerText = "Copy";
                            button.classList.remove("copied");
                        }, 1500);
                    });
                };

                pre.style.position = "relative";
                pre.appendChild(button);
            }
        });
    });

    // Back link
    let path = window.location.pathname;
    let segments = path.split('/').filter(segment => segment !== "");
    if (segments.length > 1) {
        segments.pop();
    }
    let newPath = '/' + segments.join('/');
    document.getElementById("backLink").setAttribute("href", newPath);
</script>