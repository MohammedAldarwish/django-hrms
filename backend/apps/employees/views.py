from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


class EmployeeView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new Employee.

        Expects the employee fields in the request body (JSON).
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """Delete an employee.

        Accepts an `id` either as a query param (`/emp?id=1`) or in the
        request body JSON (`{"id": 1}`). Returns 204 on success.
        """
        emp_id = request.query_params.get("id") or request.data.get("id")
        if not emp_id:
            return Response({"detail": "Employee id required"}, status=status.HTTP_400_BAD_REQUEST)

        employee = get_object_or_404(Employee, pk=emp_id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)