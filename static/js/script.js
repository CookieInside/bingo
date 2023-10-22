function createCard(list){
    const fields = document.getElementsByClassName("textDiv");
    for(let i = 0; i < 25; i++){
        fields[i].innerHTML = list[i];
    }
}

function setup(){
    const inputList = [];
    createCard(generateTextList(inputList));
}

let selected = [
    false, false, false, false, false,
    false, false, false, false, false,
    false, false, false, false, false,
    false, false, false, false, false,
    false, false, false, false, false
]
function select(index){
    const fields = document.getElementsByClassName("textDiv");
    if(!selected[index]){
        fields[index].style["background-color"] = "rgb(23, 212, 54)";
    }else{
        fields[index].style["background-color"] = "rgb(147, 138, 148)";
    }
    
    selected[index] = !selected[index];

    if(checkWin() == true){
        alert("You Won!");
    }

}


function checkWin(){
    const listed = [];
    for(i = 0; i < selected.length; i++){
        if(selected[i]){
            listed.push(i);
        }
    }
    let possibleWins = [
        [0,1,2,3,4],
        [5,6,7,8,9],
        [10,11,12,13,14],
        [15,16,17,18,19],
        [20,21,22,23,24],
        [0,5,10,15,20],
        [1,6,11,16,21],
        [2,7,12,17,22],
        [3,8,13,18,23],
        [4,9,14,19,24],
        [0,6,12,18,24],
        [4,8,12,16,20]
    ];
    
    let win;
    for(const i of possibleWins){
        win = true;
        for(j of i){
            if(selected[j] == false){
                win = false;
            }
        }
        if(win == true){
            return(true);
        }
    }
    return(false);
}

function generateTextList(inList){
    out = []
    if(inList.length >= 25){
        for(let i = 0; i < 25; i++){
            const randomIndex = Math.floor(Math.random() * inList.length);
            out.push(inList[randomIndex]);
            inList.splice(randomIndex, 1);
        }
    }
    return(out);
}

window.onload = setup