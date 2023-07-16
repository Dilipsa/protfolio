jQuery('#profile_form').validate({
  rules: {
      home_address: {
          maxlength: 255
      },
      phone_number: {
          required: true,
          customphone: true
      },
      latitude: {
          required: function(element) {
              return jQuery('#id_longitude').val().trim().length > 0 || jQuery('#id_phone_number').val().trim().length > 0;
          },
          number: true,
          min: -90,
          max: 90
      },
      longitude: {
          required: function(element) {
              return jQuery('#id_latitude').val().trim().length > 0 || jQuery('#id_phone_number').val().trim().length > 0;
          },
          number: true,
          min: -180,
          max: 180
      }
  },
  messages: {
      home_address: {
          maxlength: "Maximum 255 characters please",
          required: "Please enter home address",
      },
      phone_number: {
          required: "Please enter your mobile number",
          customphone: "Please enter a valid Indian mobile number"
      },
      latitude: {
          required: "Please enter latitude",
          number: "Please enter a valid latitude",
          min: "Latitude must be between -90 and 90",
          max: "Latitude must be between -90 and 90"
      },
      longitude: {
          required: "Please enter longitude",
          number: "Please enter a valid longitude",
          min: "Longitude must be between -180 and 180",
          max: "Longitude must be between -180 and 180"
      }
  },
  submitHandler: function(form) {
      if (this.errorList.length === 0) {
          form.submit();
      }
  }
});

jQuery.validator.addMethod("customphone", function(value, element) {
  return this.optional(element) || /^(0|(\+91(\s|-)?))?[6789]\d{9}$/.test(value);
}, "Please enter a valid Indian mobile number.");
