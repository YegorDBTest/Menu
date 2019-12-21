$(document).ready(function() {
  getDishes(true);

  $('#dishForm').submit(function(e) {
    e.preventDefault();

    var data = new FormData(this);
    $.ajax({
      url: createDishUrl,
      data: data,
      type: "POST",
      processData: false,
      contentType: false,
    })
    .done(function(dish) {
      drawDish(dish, true, 'prepend');
      $('#dishFormModal').modal('hide');
    })
    .fail(ajaxFailHandle);
  });

  $('body').delegate('.dish-checkbox', 'change', function(e) {
    let dishesIds = [];
    for (let checkbox of $('.dish-checkbox:checked')) {
      dishesIds.push($(checkbox).attr('dish-id'));
    }
    document.cookie = `order-dishes=${dishesIds.join()}`;
  });
});
