from ninja import Router

router = Router()


@router.get("")
def health_check(request):
    return {"status": "up"}
