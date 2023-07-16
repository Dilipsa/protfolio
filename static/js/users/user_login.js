$('#login_form').validate({
  rules: {
    login: {
      required: true,
      email: true
    },
    password: {
      required: true
    }
  },
  messages: {
    login: {
      required: "Please enter your email address",
      email: "Please enter a valid email address"
    },
    password: {
      required: "Please enter your password"
    }
  }
});
