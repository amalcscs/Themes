/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
   const toggle = document.getElementById(toggleId),
         nav = document.getElementById(navId)

   toggle.addEventListener('click', () =>{
       // Agregar clase show-menu a nav menu
       nav.classList.toggle('show-menu')
       // Agregar show-icon para mostrar y ocultar el icono del menú
       toggle.classList.toggle('show-icon')
   })
}

showMenu('nav-toggle','nav-menu')

/*=============== SHOW DROPDOWN MENU ===============*/
const dropdownItems = document.querySelectorAll('.dropdown__item')

// 1. Selecionar cada dropdown item
dropdownItems.forEach((item) =>{
    const dropdownButton = item.querySelector('.dropdown__button') 

    // 2. Selecionar cada click del botón
    dropdownButton.addEventListener('click', () =>{
        // 7. Seleccionar la clase show-dropdown actual
        const showDropdown = document.querySelector('.show-dropdown')
        
        // 5. Llamar a la funcion toggleItem
        toggleItem(item)

        // 8. Remover la clase show-dropdown de otros items
        if(showDropdown && showDropdown!== item){
            toggleItem(showDropdown)
        }
    })
})

// 3. Crear una función para mostrar el dropdown
const toggleItem = (item) =>{
    // 3.1. Selecionar cada dropdown content
    const dropdownContainer = item.querySelector('.dropdown__container')

    // 6. Si el mismo item contiene la clase show-dropdown, remover
    if(item.classList.contains('show-dropdown')){
        dropdownContainer.removeAttribute('style')
        item.classList.remove('show-dropdown')
    } else{
        // 4. Agregar el height maximo al dropdown content y agregar la clase show-dropdown
        dropdownContainer.style.height = dropdownContainer.scrollHeight + 'px'
        item.classList.add('show-dropdown')
    }
}

/*=============== DELETE DROPDOWN STYLES ===============*/
const mediaQuery = matchMedia('(min-width: 1118px)'),
      dropdownContainer = document.querySelectorAll('.dropdown__container')

// Función para eliminar estilos desplegables en modo móvil cuando el navegador cambia de tamaño
const removeStyle = () =>{
    // Validar si la media query llega a 1118px
    if(mediaQuery.matches){
        // Removemos el estilo de height de dropdown container
        dropdownContainer.forEach((e) =>{
            e.removeAttribute('style')
        })

        // Removemos la clase show-dropdown de dropdown item
        dropdownItems.forEach((e) =>{
            e.classList.remove('show-dropdown')
        })
    }
}

addEventListener('resize', removeStyle)


/*=============== SHOW SCROLL UP ===============*/ 
const scrollUp = () =>{
	// const scrollUp = document.getElementById('scroll-up')
    const scrollWh = document.getElementById('scroll-wh')
    // When the scroll is higher than 350 viewport height, add the show-scroll class to the a tag with the scrollup class
	// this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
	// 					: scrollUp.classList.remove('show-scroll')
    this.scrollY >= 350 ? scrollWh.classList.add('show-scroll')
						: scrollWh.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)



// ************* Reduce the Height of Navbar ********

window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    var scrollPosition = window.scrollY || window.pageYOffset;
  
    if (scrollPosition > 0) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });




// *********Showing the Active Link ********88

// Get the current URL path
var currentPath = window.location.pathname;

// Get all the navigation links
var navLinks = document.querySelectorAll('.nav__menu li a');

// Loop through the navigation links
for (var i = 0; i < navLinks.length; i++) {
  var linkPath = navLinks[i].getAttribute('href');

  // Check if the link's href matches the current path
  if (linkPath === currentPath) {
    // Add the 'active' class to the link
    navLinks[i].classList.add('active');
  }
}


// image chenge on background top section

const bg =document.getElementById('');
window.addEventListener('scroll',function()
{
  bg.style.backgroundSize = 100 - +this.window.pageYOffset/12+'%';
  bg.style.opacity = 1- +this.window.pageXOffset/700 +'';
})








