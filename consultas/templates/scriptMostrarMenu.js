const links = document.querySelectorAll('.abrir-menu');

links.forEach(link => {
  link.addEventListener('click', function(event) {
    event.preventDefault(); 
    
    const allDivs = document.querySelectorAll('.menu');
    allDivs.forEach(div => {
      div.style.display = 'none';
    });

    const targetDivClass = this.getAttribute('data-target');
    const targetDiv = document.querySelector(`.${targetDivClass}`);
    targetDiv.style.display = 'block';

    targetDiv.addEventListener('mouseleave', function() {
        targetDiv.style.display = 'none';
    });

  });
});
