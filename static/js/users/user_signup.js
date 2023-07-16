$('#signup_form').validate({
  rules: {
    email: {
      required: true,
      email: true,
      remote: {
        url: '/users/check-email-registered/',
        type: 'GET',
        data: {
          email: function() {
            return $('#id_email').val();
          }
        },
        dataFilter: function(data) {
          var response = JSON.parse(data);
          if (response.registered === true) {
            return '"This email is already registered."';
          } else {
            return 'true';
          }
        }
      }
    },
    password1: {
      required: true,
      minlength: 8,
      strongPassword: true
    },
    password2: {
      required: true,
      equalTo: '#id_password1'
    }
  },
  messages: {
    email: {
      required: "Please enter your email address",
      email: "Please enter a valid email address",
      remote: "This email is already registered."
    },
    password1: {
      required: "Please enter your password",
      minlength: "Password must be at least 8 characters long",
    },
    password2: {
      required: "Please enter your password",
      equalTo: "Passwords do not match"
    }
  }
});

// Custom validation method for strong password
$.validator.addMethod("strongPassword", function(value, element) {
  // Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/g.test(value);
}, "Please choose a stronger password (at least 8 characters long \
  and should include at least one uppercase letter, one lowercase letter, \
  one digit, and one special character)");
