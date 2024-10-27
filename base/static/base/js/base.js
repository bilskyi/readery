function openTab(evt, tabName) { 
    var i, tabcontent, tablinks; 

    // Hide all tab content 
    tabcontent = document.getElementsByClassName("tabcontent"); 
    for (i = 0; i < tabcontent.length; i++) { 
        tabcontent[i].style.display = "none"; 
    } 

    // Remove "active" class from all tab links 
    tablinks = document.getElementsByClassName("tablinks"); 
    for (i = 0; i < tablinks.length; i++) { 
        tablinks[i].className = tablinks[i].className.replace(" active", ""); 
    } 

    // Show the current tab and add "active" class to the clicked tab link 
    document.getElementById(tabName).style.display = "block"; 
    evt.currentTarget.className += " active"; 
} 

// Toggle visibility of the add new book form 
function toggleForm() { 
    const form = document.querySelector('#books .form-container'); 
    form.style.display = form.style.display === 'none' ? 'block' : 'none'; 
} 

// Toggle visibility of the add new author form 
function toggleAuthorForm() { 
    const form = document.querySelector('#authors .form-container'); 
    form.style.display = form.style.display === 'none' ? 'block' : 'none'; 
} 

// Toggle visibility of the add new genre form 
function toggleGenreForm() { 
    const form = document.querySelector('#genres .form-container'); 
    form.style.display = form.style.display === 'none' ? 'block' : 'none'; 
} 

// Toggle visibility of the add new order item form 
function toggleOrderForm() { 
    const form = document.querySelector('#orders .form-container'); 
    form.style.display = form.style.display === 'none' ? 'block' : 'none'; 
} 

// Toggle visibility of the create new bill form 
function toggleBillForm() { 
    const form = document.querySelector('#bill .form-container'); 
    form.style.display = form.style.display === 'none' ? 'block' : 'none'; 
} 

// Placeholder functions for adding new records 
function addBook() { /* Add new book logic */ } 
function addAuthor() { /* Add new author logic */ } 
function addGenre() { /* Add new genre logic */ } 
function addOrder() { /* Add new order logic */ } 
function addBill() { /* Add new bill logic */ } 

// Placeholder functions for updating records 
function updateBook(button) { /* Update book logic */ } 
function updateAuthor(button) { /* Update author logic */ } 
function updateGenre(button) { /* Update genre logic */ } 
function updateOrder(button) { /* Update order logic */ } 
function updateBill(button) { /* Update bill logic */ } 

// Placeholder functions for deleting records 
function deleteBook(button) { /* Delete book logic */ } 
function deleteAuthor(button) { /* Delete author logic */ } 
function deleteGenre(button) { /* Delete genre logic */ } 
function deleteOrder(button) { /* Delete order logic */ } 
function deleteBill(button) { /* Delete bill logic */ } 

// Placeholder functions for filtering records 
function filterBooks(criteria) { /* Filter books logic */ } 
function filterAuthors(criteria) { /* Filter authors logic */ } 
function filterGenres(criteria) { /* Filter genres logic */ } 
function filterOrders(criteria) { /* Filter orders logic */ } 
function filterBills(criteria) { /* Filter bills logic */ } 

// By default, open the first tab 
document.addEventListener("DOMContentLoaded", function() { 
document.querySelector('.tablinks').click(); 
}); 
