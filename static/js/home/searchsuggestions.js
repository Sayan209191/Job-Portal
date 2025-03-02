document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const suggestionsBox = document.getElementById("suggestions-box");

    searchInput.addEventListener("input", function () {
        let query = searchInput.value.trim();
        if (query.length < 2) { 
            suggestionsBox.innerHTML = ""; 
            return; 
        }

        fetch(`/search-suggestions/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                suggestionsBox.innerHTML = "";
                if (data.suggestions.length > 0) {
                    data.suggestions.forEach(suggestion => {
                        let div = document.createElement("div");
                        let highlightedText = suggestion.replace(new RegExp(query, "gi"), (match) => `<strong>${match}</strong>`);
                        div.innerHTML = highlightedText;
                        div.classList.add("suggestion-item");
                        div.addEventListener("click", function () {
                            searchInput.value = suggestion;
                            suggestionsBox.innerHTML = "";
                        });
                        suggestionsBox.appendChild(div);
                    });
                }
            });
    });

    document.addEventListener("click", function (e) {
        if (!searchInput.contains(e.target) && !suggestionsBox.contains(e.target)) {
            suggestionsBox.innerHTML = "";
        }
    });
});