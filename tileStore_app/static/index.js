const toggleButton= document.getElementsByClassName('toggle-button')[0]
const navbarLinks=document.getElementsByClassName('links_section')[0]

toggleButton.addEventListener('click',()=>{
    navbarLinks.classList.toggle('active')
})


// get elements for popup

const popupbtn = document.querySelector('.popupbtn');

const popup = document.querySelector('.popup-wrapper');

const popupclose = document.querySelector('.popup-close');

// popup

popupbtn.addEventListener('click',() =>{

    popup.style.display = "block";

    console.log("opening modal");

});

popupclose.addEventListener('click', () => {

    popup.style.display = 'none';

});

popup.addEventListener('click', (e) => {

    if(e.target.className === 'popup-wrapper'){

      popup.style.display = 'none';

    }

});