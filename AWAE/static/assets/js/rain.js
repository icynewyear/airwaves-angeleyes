function send_seed() {

  $.ajax({
      type: "GET",
      url: "/trunk/seed/word",
      data: {"word": input},
      success: function(result) {
      },
      error: function(result) {
      }
});
};
