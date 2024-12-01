const totalPages = 100; // Total number of pages
const paginationContainer = document.getElementById('pagination-container');
const maxVisibleButtons = 10; // Maximum number of buttons to show at once

function generatePagination() {
    // Clear the container before generating new pagination buttons
    paginationContainer.innerHTML = '';

    // Show "Previous" button
    const prevButton = document.createElement('button');
    prevButton.classList.add('pagination-button');
    prevButton.innerText = 'Previous';
    paginationContainer.appendChild(prevButton);

    // Show page numbers with ellipses
    let pageNumbers = [];
    for (let i = 1; i <= totalPages; i++) {
        pageNumbers.push(i);
    }

    if (pageNumbers.length > maxVisibleButtons) {
        pageNumbers = [
            ...pageNumbers.slice(0, 3), // Show first 3 pages
            '...',
            ...pageNumbers.slice(pageNumbers.length - 3) // Show last 3 pages
        ];
    }

    // Create buttons for visible page numbers
    pageNumbers.forEach((page) => {
        const button = document.createElement('button');
        button.classList.add('pagination-button');
        if (page === '...') {
            button.classList.add('ellipsis');
            button.innerText = '...';
        } else {
            button.setAttribute('data-page', page);
            button.innerText = page;
        }
        paginationContainer.appendChild(button);
    });

    // Show "Next" button
    const nextButton = document.createElement('button');
    nextButton.classList.add('pagination-button');
    nextButton.innerText = 'Next';
    paginationContainer.appendChild(nextButton);
}

// Call the function to generate pagination when the page loads
generatePagination();