$(document).ready(function(){

    setInterval(function(){
        $.ajax({
            type: 'GET',
            data:{
                pk:1
            },
            url: 'http://127.0.0.1:8000/lists/1/tasks/',
            // url: '{% url "get_tasks" pk=lista.pk %}',
            success: function(data){
                $('#tasks_list').empty();
                for (var task in data.tasks){
                    var temp = '<li>'+ data.tasks[task].title +' </li>';
                    if (data.tasks[task].done == false){
                        temp = temp + '<a href="{% url 'toggle_done' pk=lista.pk id=task.id mark=done %}"> mark as done </a>'
                    }else{
                        temp = temp + '<a href="{% url 'toggle_done' pk=lista.pk id=task.id mark=undone %}"> mark as not done </a>'
                    };
                    $('#tasks_list').append(temp);
                }
                
            },
        });

    },1000);




});