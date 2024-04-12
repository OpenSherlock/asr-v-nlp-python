from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import simplejson as json
from .predicatedetector import handleSingleSentence #handleSentences
from .util import check_json
print('APP starting')
async def process(request):
    print('GOT', request)
    '''
    request = a JSON Object := {'sentences':[array]}
    '''
    json = await request.json()

    print('Debug:', json)
    result = handleSingleSentence(json)
    # print('FINAL', result)
    return JSONResponse(json.dumps(result))

routes = [
    Route('/',process, methods=['POST'])
]
app = Starlette(debug=True, routes=routes)

