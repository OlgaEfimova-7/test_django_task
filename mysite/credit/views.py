from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from credit.models import Contract, CreditRequest, Producer, Product

# Create your views here.


@api_view(["GET",])
def get_producers_by_contract(request):
    """View to get all unique producers of all products in credit request,
    related to the specific contract"""
    contract_id = request.query_params.get("contract_id")

    credit_request_obj = (
        CreditRequest.objects.filter(contract_id=contract_id).only("id").first()
    )

    if not credit_request_obj:
        return Response({"ERROR": f"NOT FOUND credit_request BY contract_id {contract_id}"})

    producers_ids = (
        Product.objects.select_related("producer")
        .filter(credit_request_id=credit_request_obj.id)
        .distinct("producer_id")
        .values_list("producer_id", flat=True)
    )

    # It is possible to obtain all necessary information through the Product model. 
    # In this case database queries can be minimized to one:
        # producers_ids = (
        #     Product.objects.select_related("credit_request")
        #     .select_related("producer")
        #     .select_related("credit_request__contract")
        #     .filter(credit_request__contract__id=contract_id)
        #     .distinct("producer_id")
        #     .values_list("producer_id", flat=True)
        # )

    return Response({"producer_ids": producers_ids})
