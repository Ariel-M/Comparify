


(function (){
  
  let walmart_price = document.querySelector('#price');
  let ebay_price = document.querySelector('#ebayPrice');
  if (walmart_price.value < ebay_price){
   walmart_price.style.color = 'green';
  }else if(ebay_price < walmart_price){
    ebay_price.style.color = 'green';
  }else{
    walmart_price.style.color = 'green';
    ebay_price.style.color = 'green';
    
  }
})();

