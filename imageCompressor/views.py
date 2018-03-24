from django.shortcuts import render, redirect
import os
from imageCompressor.compressor import compressImage
# Create your views here.

def index(request):
	#  Home page
	return render(request, 'imageCompressor/home.html')


def upload(request):
	#  Get uploaded file
	if request.method == 'POST':
		#  Check if the uploaded image file is of type jpg or not
		if not str(request.FILES['file']).endswith('jpg'):
			return render(request, 'imageCompressor/error.html')

		handleUploadedFile(request, request.FILES['file'], str(request.FILES['file']))
		#  Rename the image file, so it becomes easier to refer
		os.rename('imageCompressor/upload/' + str(request.FILES['file']), 'imageCompressor/upload/1.jpg')
		#  Get this attribute from user
		quality = request.POST.get('quality', '')
		#  Compress the image, this function is written in compressor.py file
		compressImage(quality)
		#  Get image file properties
		fullSize = os.stat('imageCompressor/upload/1.jpg')
		compressedSize = os.stat('imageCompressor/upload/resized-image.jpg')
		#  Display both full size and compressed images
		return render(request, 'imageCompressor/success.html', {'fullSizeUrl': '1.jpg', 'compressedUrl': 'resized-image.jpg', 'fullSizeSize': int(fullSize.st_size / 1000) , 'compressedSize': int(compressedSize.st_size / 1000)})
	return render(request, 'imageCompressor/home.html')


#  Function to move the file to upload directory
def handleUploadedFile(request, file, filename):
		if not os.path.exists('imageCompressor/upload/'):
			os.mkdir('imageCompressor/upload/')
		with open('imageCompressor/upload/' + filename, 'wb+') as destination:
			for chunk in file.chunks():
				destination.write(chunk)
