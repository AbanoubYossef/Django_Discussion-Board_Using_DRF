from django.shortcuts import get_object_or_404, redirect, render
import requests
import json
# Create your views here.
def boards_list(request):
    backend_url = "http://127.0.0.1:8000/boards/"
    headers = {'content-type': "Application/jason"}
    response = requests.get(backend_url, headers=headers)
    boards = response.json()
    return render(request, 'home.html', {'boards':boards})

def board_topics(request,board_id):
    backend_url = f"http://127.0.0.1:8000/boards/{board_id}/"
    headers = {'content-type': "Application/jason"}
    response = requests.get(backend_url, headers=headers)
    topics_details = response.json()
    
    backend_url_2 =f"http://127.0.0.1:8000/boards/board_details/{board_id}/"
    resopnse_board = requests.get(backend_url_2, headers= headers)
    board_details= resopnse_board.json()
    
    return render(request,'topics.html', {'board':board_details,"topics":topics_details})


def new_topic(request, board_id):
    # Define backend URLs
    backend_url = f"http://127.0.0.1:8000/boards/{board_id}/"
    backend_url_2 = f"http://127.0.0.1:8000/boards/board_details/{board_id}/"
    headers = {'content-type': "application/json"}
    # Retrieve board details from backend
    response_board = requests.get(backend_url_2, headers=headers)
    board_details = response_board.json()

    if request.method == "POST":
        # Retrieve form data
        subject = request.POST['subject']
        message = request.POST['message']
        created_by = 1  

        data = json.dumps({
            "subject": subject,
            "message": message,
            "created_by": created_by,
            "board": board_id  
        })
        # Make POST request to create a new topic
        response_topic = requests.post(backend_url, headers=headers, data=data)
        print(response_topic.json())
        return redirect('topics', board_id=board_id)
    
    # Render the form to create a new topic
    return render(request, 'new_topic.html', {'board': board_details})
