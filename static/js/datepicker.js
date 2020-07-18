$("#id_date").datepicker({
  dateFormat: "mm-dd-yy",
  showButtonPanel: true,
  closeText: "Close",
  beforeShow: function (input, inst) {
      setTimeout(function () {
          inst.dpDiv.css({
              top: $("#id_date").offset().top + 35,
              left: $("#id_date").offset().left
          });
      }, 0);
  },
});
