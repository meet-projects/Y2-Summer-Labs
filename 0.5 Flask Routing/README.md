# Let's build our own Ebay! - Flask Routing Lab
<br/>
Today, we are creating <b>an awesome online shop similar to Ebay!</b>
<br/>

In our project folder, we have a <b>'static' folder</b> which will be used for <b>css and js files</b>, and a <b>'templates' folder</b> where you'll find all of our <b>templates (html files)</b> that we are/will be using.
<br/>
In today's lab, you'll only work with and edit one main Python file and 3 templates: <b>home.html, product.html and cart.html</b>.
<br/>
 


### First things first, *fork* this repo(sitory) and *clone* it to your desktop!

## Part 1: Home
1. Create your first app route and link it to `home.html` in `app.py`. 
2. Give `home.html` some life! Some things you can add:
    - Shop name
    - Description
    - Image of some things you sell
    - Sections or categories of items
    - Strech goal - try to make it as much similar as possible to this:
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/0.5%20Flask%20Routing/ebayHomepage.png" width="700">
(Don't link anything yet, keep the href empty. Like: href="#" or href=" ")

## Part 2: Product Page
1. Create an another app route in `app.py` and link it to `product.html`.
2. Update the "Product" link(s) in `home.html` according to the new app route.
3. Give `product.html` some life! Some things you can add:
    - Title
    - Image
    - Description
    - Price
    - Link back to your homepage.
    - Try to make it as much similar as possible to this:
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/0.5%20Flask%20Routing/ebayProduct.png" width="700">
    
    - Optionally: If you want to style, link for reference: https://www.w3schools.com/howto/howto_css_product_card.asp )

## Part 3: Cart
1. Create an another app route in `app.py` and link it to the template `cart.html`
2. Update the "Cart" link in `home.html` and `product.html` according to the new app route.
3. Modify the products elements in `home.html` and link the "Add to Cart" button to the new route that you just created.
* We will not be creating the "Add to Cart" function today, but this will help us set it up for the upcoming sessions.
4. Fill in some content products in the cart, for preview purposes only.
    - Try to make it as much similar as possible to this:
    <img src="https://github.com/meet-projects/Y2-Summer-Labs/blob/master/0.5%20Flask%20Routing/ebayCart.png" width="700">

### Bonus:
- Add a navigation bar to all pages - and link all tabs. (if you haven't yet)
- Add a carousel in your homepage.
- Complete all of your pages designs, fill in the gaps of what's missing!
