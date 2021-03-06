function getOrderDishesIds() {
  let value = document.cookie.split('order-dishes=')[1].split(';')[0];
  if (value.length == 0) return [];
  return value.split(',');
}
var orderDishesIds = getOrderDishesIds();


function drawDish(dish, onMain, addKind='append') {
  let dishesBox = onMain ? $(`#category${dish.category}`) : $('#dishesBox');
  if (dishesBox) {
    let checkbox = '';
    if (onMain) {
      let checked = orderDishesIds.includes(dish.id.toString()) ? 'checked' : '';
      checkbox = `<input type="checkbox" class="dish-checkbox" dish-id="${dish.id}" ${checked}>`;
    }
    dishesBox[addKind](`
      <div class="col-md-4">
        ${checkbox}
        <div>
          <h4>${dish.name}</h4>
        </div>
        <div>
          <img src="${dish.picture}" height="300" width="300">
        </div>
        <div class="row">
          <span class="col-md-4">Белки</span>
          <span class="col-md-8">${dish.squirrels} г.</span>
          <span class="col-md-4">Жиры</span>
          <span class="col-md-8">${dish.fats} г.</span>
          <span class="col-md-4">Углеводы</span>
          <span class="col-md-8">${dish.carbohydrates} г.</span>
          <span class="col-md-4">Энергетическая ценность</span>
          <span class="col-md-8">${dish.energy} кКал.</span>
          <span class="col-md-4">Стоимость</span>
          <span class="col-md-8">${dish.price} руб.</span>
          <span class="col-md-4">Аллергены</span>
          <span class="col-md-8">${dish.allergens}</span>
        </div>
      </div>
    `);
  }
}


function drawTotal(totalData) {
  $('#allergensBox').append(totalData.allergens.join(', '));
  $('#priceBox').append(totalData.price);
}


function ajaxFailHandle(jqXHR, textStatus, errorThrown) {
  console.log('jqXHR', jqXHR);
  console.log('textStatus', jqtextStatusXHR);
  console.log('errorThrown', errorThrown);
}


function getDishes(onMain=false) {
  var data = {};
  if (!onMain) data['ids'] = orderDishesIds.join();
  if (!onMain) data['tn'] = 1;
  $.ajax({
    url: getDishesUrl,
    data: data,
    type: "GET",
  })
  .done(function(data) {
    for (let dish of data.dishes) {
      drawDish(dish, onMain);
    }
    if (data.total) {
      drawTotal(data.total);
    }
  })
  .fail(ajaxFailHandle);
}
