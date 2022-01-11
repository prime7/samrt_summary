from api.models import Summary
from rest_framework.generics import CreateAPIView,GenericAPIView, get_object_or_404
from rest_framework import permissions, status
from api.serializers import SummarySerializer,RateSummarySerializer
from rest_framework.response import Response


class SummaryAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = SummarySerializer

    def post(self,request):
        serializer = SummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummaryReviewAPIView(GenericAPIView):
    permission_classes = [ permissions.AllowAny,]
    serializer_class = RateSummarySerializer
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sid = serializer.data['summary_id']
        summary = get_object_or_404(Summary,pk=sid)
        summary.rating = serializer.data['rate']
        summary.save()
        
        return Response({"msg":"Rating saved succesfully"},status=status.HTTP_200_OK)
