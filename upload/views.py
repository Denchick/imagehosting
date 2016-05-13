from django.shortcuts import render, get_object_or_404
from .models import Image

def main(request):
	return render(request, 'upload/index.html', {})

def image_detail(request, pk):
	image = get_object_or_404(Image, pk=pk)
	return render(request, 'upload/image_detail.html', {'image' : image})
