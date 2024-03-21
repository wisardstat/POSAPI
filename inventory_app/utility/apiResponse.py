from fastapi.responses import JSONResponse

class ApiResponse:
    def __init__(self, status_code: int , status: str, message: str, data: dict | list | None = None, error: dict | None = None):
        self.status_code = status_code
        self.status= status
        self.message = message
        self.data = data
        self.error = error

    def to_json(self) -> JSONResponse:
        response = {}
        if self.status:
            response["status"] = self.status
        if self.message:
            response["message"] = self.message
        if self.data:
            response["data"] = self.data
        if self.error:
            response["error"] = self.error
        return JSONResponse(status_code=self.status_code, content=response)

def response(status_code: int, status: str, message: str, data: dict | list | None = None, error: dict | None = None) -> JSONResponse:
    response = ApiResponse(status_code,status, message, data, error)
    print(response)
    return response.to_json()