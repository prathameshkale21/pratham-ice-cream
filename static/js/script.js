document.addEventListener("DOMContentLoaded", function () {

    const popups = document.querySelectorAll(".popup-message");

    popups.forEach(function (popup, index) {

        // Slight stagger so multiple toasts don't all pop in at once
        setTimeout(() => {
            popup.classList.add("show");
        }, index * 150);

        const closeBtn = popup.querySelector(".popup-close");

        function hidePopup() {

            popup.classList.remove("show");

            setTimeout(() => {

                popup.remove();

            }, 400);

        }

        closeBtn.addEventListener("click", hidePopup);

        // Disposable toast: auto-dismiss on its own after a few seconds
        setTimeout(hidePopup, 3500 + index * 150);

    });

});
