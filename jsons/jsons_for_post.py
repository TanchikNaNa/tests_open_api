class class_jsons_for_post_requests:
    body_CREATE = {
    "name": "morpheus",
    "job": "leader"
}
    body_LOGIN_UNSUCCESSFUL = {
    "email": "peter@klaven"
}

class class_jsons_for_post_responses:
    body_CREATE_ans = str({
    "name": "morpheus",
    "job": "leader",
    "id": "0",
    "createdAt": "0"
})
    
    body_LOGIN_UNSUCCESSFUL_ans = str({
    "error": "Missing password"
})
