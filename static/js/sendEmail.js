function sendMail(contactForm) {
    emailjs.send("gmail", "contactus", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "contact_us": contactForm.contactus.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page - this will allow for a user to send messages to the company
}