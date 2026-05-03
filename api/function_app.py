import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="CalculateArea", auth_level=func.AuthLevel.ANONYMOUS)
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        shape = req_body.get('shape')
        data = req_body.get('data')
        area = 0
        if shape == 'square':
            area = data['side'] ** 2
        elif shape == 'rectangle':
            area = data['width'] * data['height']
        elif shape == 'circle':
            area = 3.14159 * (data['radius'] ** 2)
        elif shape == 'triangle':
            area = 0.5 * data['base'] * data['height']
        return func.HttpResponse(
            json.dumps({"area": area}),
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )
