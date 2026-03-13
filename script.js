// CART DATA LOCAL STORAGE SE LOAD

let cart = JSON.parse(localStorage.getItem("cart")) || [];


// ADD PRODUCT TO CART

function addToCart(name, price, image) {

    let product = {
        name: name,
        price: price,
        image: image
    };

    cart.push(product);

    localStorage.setItem("cart", JSON.stringify(cart));

    alert(name + " added to cart");
}


// LOAD CART ITEMS

function loadCart() {

    let cartList = document.getElementById("cartList");

    if (!cartList) return;

    cartList.innerHTML = "";

    let total = 0;

    cart.forEach((item, index) => {

        total += item.price;

        cartList.innerHTML += `
        
        <div class="cartItem">

            <img src="${item.image}" alt="product">

            <div class="cartDetails">

                <h3>${item.name}</h3>

                <p class="cartPrice">₹${item.price}</p>

            </div>

            <button class="removeBtn" onclick="removeItem(${index})">Remove</button>

        </div>

        `;

    });

    document.getElementById("totalPrice").innerText = "₹" + total;
}


// REMOVE PRODUCT

function removeItem(index) {

    cart.splice(index, 1);

    localStorage.setItem("cart", JSON.stringify(cart));

    loadCart();
}


// PLACE ORDER

function placeOrder() {

    if (cart.length === 0) {

        alert("Cart is empty");

        return;
    }

    alert("Order placed successfully!");

    cart = [];

    localStorage.removeItem("cart");

    loadCart();
}


// AUTO LOAD CART PAGE

window.onload = function () {

    loadCart();

};