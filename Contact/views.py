from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactFormSerializer
from django.db import IntegrityError  # Import for database error handling

@api_view(['POST'])
def submit_contact_form(request):
    if request.method == 'POST':
        try:
            serializer = ContactFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Form submitted successfully'})
            return Response(serializer.errors, status=400)
        except IntegrityError as db_error:  # Handle database errors
            return Response({'error': 'Database error occurred'}, status=500)
        except Exception as server_error:  # Handle server errors
            return Response({'error': 'Server error occurred'}, status=500)
    return Response({'error': 'Method not allowed'}, status=405)
