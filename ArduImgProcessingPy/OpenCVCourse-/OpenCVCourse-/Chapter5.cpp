#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>


using namespace cv;
using namespace std;


/////////////////// Warp Images //////////////////////

float w = 250, h = 350;
Mat matrix, imgWarp;
int srcCW[4] = { 1, 3, 0, 2 };

void main() {

	string path = "Resources/cards.jpg";
	Mat img = imread(path);

	Point2f srcK[4] = { {529,142},{771, 190}, {405,395}, {674,457} };
	Point2f dst[4] = { {0.0f,0.0f},{w, 0.0f},{0.0f,h},{w,h} };

	matrix = getPerspectiveTransform(srcK, dst);
	warpPerspective(img, imgWarp, matrix, Point(w, h));


	for (int i = 0; i < 4; i++) {
		line(img, srcK[i], srcK[srcCW[i]], Scalar(255, 0, 0), 4);
	}

	for (int i = 0; i < 4; i++) {
		circle(img, srcK[i], 3, Scalar(0, 0, 255), FILLED);
		circle(img, srcK[i], 10, Scalar(0, 0, 255), 3);
	}


	imshow("Image", img);
	imshow("Image Warp", imgWarp);

	waitKey(0);

}