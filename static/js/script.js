$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
});


/* Code for toggling password visibility, adapted from W3Schools */
function togglePasswordVisibility() {
    var passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}

/* Interactive star rating system used in write_review.html */
document.addEventListener('DOMContentLoaded', function() {
    const ratingIcons = document.querySelectorAll('.star1');
  
    ratingIcons.forEach((ratingIcon, index) => {
      ratingIcon.addEventListener('click', function() {
        
        ratingIcons.forEach((star, idx) => {
          star.classList.remove('filled');
        });
  
        
        for (let i = 0; i <= index; i++) {
          ratingIcons[i].classList.add('filled');
        }
  
        // Set the value of the hidden input field to the current rating
        document.getElementById('user_rating').value = index + 1;
      });
    });
  });
  

  