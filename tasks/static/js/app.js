
document.addEventListener("DOMContentLoaded", function () {



    var addNewTask = document.getElementById("add-new-task")
    var cancleNewTask = document.getElementById("cancle-new-task")
    addNewTask.addEventListener("click", () => {
        document.getElementById("overlay").style.display = "block";
        document.querySelector("#popout").style.display ="flex";        
    });
    cancleNewTask.addEventListener("click", () => {
        document.getElementById("overlay").style.display = "none";
        document.querySelector("#popout").style.display ="none";        
    });



//timer

var tasks = document.getElementsByClassName("taskCountdown")




    function getTimeRemaining(endtime) {
        const total = Date.parse(endtime) - Date.parse(new Date());
        const seconds = Math.floor((total / 1000) % 60);
        const minutes = Math.floor((total / 1000 / 60) % 60);
        const hours = Math.floor((total / (1000 * 60 * 60)) % 24);
        const days = Math.floor(total / (1000 * 60 * 60 * 24));
        
        return {
          total,
          days,
          hours,
          minutes,
          seconds
        };
      }


    function initializeClock(item, endtime) {
        //const clock = document.getElementById(id);
        const daysSpan = item.querySelector('.days');
        const hoursSpan = item.querySelector('.hours');
        const minutesSpan = item.querySelector('.minutes');
        const secondsSpan = item.querySelector('.seconds');

        const timeinterval = setInterval(updateClock, 1000);

        function updateClock() {
            const t = getTimeRemaining(endtime);

            daysSpan.innerHTML = t.days;
            hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
            minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
            secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

            if (t.total <= 0) {
                clearInterval(timeinterval);
                daysSpan.innerHTML = 0;
                hoursSpan.innerHTML = '00'
                minutesSpan.innerHTML = '00'
                secondsSpan.innerHTML = '00'
                daysSpan.style.backgroundColor = "#DC3545";
                hoursSpan.style.backgroundColor = "#DC3545";
                minutesSpan.style.backgroundColor = "#DC3545";
                secondsSpan.style.backgroundColor = "#DC3545";
            }
        }

        updateClock();
        
    }


    function stopClock(item){
        const daysSpan = item.querySelector('.days');
        const hoursSpan = item.querySelector('.hours');
        const minutesSpan = item.querySelector('.minutes');
        const secondsSpan = item.querySelector('.seconds');

        daysSpan.innerHTML = "D";
        hoursSpan.innerHTML = "O";
        minutesSpan.innerHTML = "N";
        secondsSpan.innerHTML = "E";

    }

    for (let item of tasks) {
        //console.log(item);
        //var matchDate = new Date(item.getAttribute('start')).getTime();
        //console.log(matchDate)
        //console.log(item.getAttribute('start'))
        const deadline = new Date(item.getAttribute('start'))
        if (item.hasAttribute('finished')) {
            const whendone = new Date(item.getAttribute('finished'))
            stopClock(item);
          }
          else{
        //console.log(deadline)
        //console.log(getTimeRemaining(deadline).total)
        initializeClock(item, deadline);}
    }


/*
    var categories = document.getElementsByClassName("delete-category")


    for (let category of categories) {
        const id = category.getAttribute('taskid')
        
        const action = "\{\% url 'tasks:delete_category' "+id+" \%\}"
        
        category.addEventListener("click", () => {
            document.querySelector(".bg-modal-category").style.display ="flex";
            //document.querySelector("#delete-category").setAttribute("action",action)
            
        });

    }*/
    

});

function overlayoff() {
    document.getElementById("overlay").style.display = "none";
    document.querySelector("#popout").style.display ="none";   
  }