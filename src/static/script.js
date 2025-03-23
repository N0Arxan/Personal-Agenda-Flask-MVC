document.addEventListener("DOMContentLoaded", () => {

    const dateInput = document.getElementById("event-date");
    const today = new Date().toISOString().split("T")[0];
    dateInput.setAttribute("min", today);

    const deleteBtn = document.getElementById("delete-user")
    deleteBtn.addEventListener("click", () => {
        fetch("/dash/deleteUser", {method: "POST"}).then(() => {
            alert("your user deleted successfully from database");
            window.location.reload();
        })
    })

    const logoutBtn = document.getElementById("logout-btn")
    logoutBtn.addEventListener("click", () => {
        fetch("/dash/logout", {method: "POST"}).then(() => {
            location.reload();
        })
    })

});


