//listening to the page load event as soon as the user make a general.
window.addEventListener('load', (e) => {
    //This event listener will listen to the page load event and as soon as the page get load it will send a fetch request to server with url(hotproperties/) and add the data inside the html tags in (details.html) page.
    e.preventDefault(); //it will prevent the page reloading
    let url = "/slider/"; //url where we are sending the fetch API request.

    let options = {
        //there are the GET method options which will go with the API request.
        method: "GET", //GET method.
        headers: {
            //headers will send the info of the content type and csrf token in the backend.
            'content-Type': "application/json",  //data type will be json.
            'X-CSRFToken': csrftoken,  //csrftoken verification.
        }
    };
    var html = ""; //empty html var to store the html elements with data.
    const PropertyContainer = document.getElementById('banner_eig_slider');  //Accessing the property element to insert the filtered properties in it.
    fetch(url, options) //fetch request.
        .then(Response => Response.json())//here we are converting the data into json format.
        .then(data => {
            // this function will append the data into the html variable and in the end it will append the html into PropertyContainer element.
            if (Object.keys(data).length != 0) {
                data.forEach(element => {
                    console.log(element)
                    //This for loop will iterate over all the element present in the data and one by one it will apppend them into the html variable.
                    html += `<div class="item"><a href="/${element.slug}/${element.Location}"><img src="${element.Property_Image}"></a></div>`;
                });
                PropertyContainer.innerHTML = html; //Appending the data into the PropertyContainer div block.
            }
        })
});
