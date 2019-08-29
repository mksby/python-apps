from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UrlSerializer
from .models import URL


class UrlsView(APIView):
    def get(self, request):
        urls = URL.objects.all()
        serializer = UrlSerializer(urls, many=True)
        return Response({"urls": serializer.data})

    def post(self, request):
        url = request.data.get('url')
        # Create an url from the above data
        serializer = UrlSerializer(data=url)
        if serializer.is_valid(raise_exception=True):
            url_saved = serializer.save()
        return Response({"success": "Url '{}' created successfully".format(url_saved.url)})

    def put(self, request, pk):
        saved_url = get_object_or_404(URL.objects.all(), pk=pk)
        data = request.data.get('url')
        serializer = UrlSerializer(instance=saved_url, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            url_saved = serializer.save()
        return Response({
            "success": "Url '{}' updated successfully".format(url_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(URL.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Url with id `{}` has been deleted.".format(pk)
        }, status=204)

class UrlDetailView(APIView):
    def get(self, request, pk):
        urls = URL.objects.filter(pk=pk)
        serializer = UrlSerializer(urls, many=True)
        return Response({"urls": serializer.data})