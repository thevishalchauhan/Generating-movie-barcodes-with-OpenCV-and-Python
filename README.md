# Generating-movie-barcodes-with-OpenCV-and-Python

### Commands:-

1. To check the Frame rate of Video
    #### python count_frames.py --video videos/jurassic_park_trailer.mp4

2. Generating the movie barcode data
    #### python generate_barcode.py --video videos/jurassic_park_trailer.mp4 --output output/jurassic_park_trailer.json --skip 25
    
3. Visualizing and saving the barcode
    #### python visualize_barcode.py --avgs output/jurassic_park_trailer.json --barcode output/jurassic_park_trailer.png --barcode-width 5
    
Reference: PyImageSearch
