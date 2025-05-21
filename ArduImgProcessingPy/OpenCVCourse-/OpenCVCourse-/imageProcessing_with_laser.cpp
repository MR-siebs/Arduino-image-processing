#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;


void findLaser(Mat imgDil, Mat img) {

	vector<vector<Point>> contours;
	vector<Vec4i> hierarchy;

	findContours(imgDil, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

	for (int i = 0; i < contours.size(); i++)
	{
		int area = contourArea(contours[i]);
		cout << area << endl;

		vector<vector<Point>> conPoly(contours.size());
		vector<Rect> boundRect(contours.size());

		if (area > 100)
		{
			float peri = arcLength(contours[i], true);
			approxPolyDP(contours[i], conPoly[i], 0.02 * peri, true);
			cout << conPoly[i].size() << endl;

			boundRect[i] = boundingRect(conPoly[i]);

			drawContours(img, conPoly, i, Scalar(255, 0, 255), 2);
			rectangle(img, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 5);
		}
	}
}

void main() {

	string path = "Resources/redDot.png";
	Mat img = imread(path);

	Mat imgGray, blueGreen(img.rows, img.cols, CV_8UC3), imgBlur, imgCanny, imgDil;


	//pre-processing
	int from_to[6] = {0,0 , 1,1, 0,2};
	mixChannels(img, blueGreen, from_to, 3 );

	cvtColor(blueGreen, imgGray, COLOR_BGR2GRAY);
	GaussianBlur(img, imgBlur, Size(3, 3), 3, 0);
	Canny(imgBlur, imgCanny, 25, 75);

	Mat kernel = getStructuringElement(MORPH_RECT, Size(3, 3));
	dilate(imgCanny, imgDil, kernel);


	findLaser(imgDil, img);


	imshow("Image", img);
	//imshow("blue/green grayscale", imgGray);
	//imshow("Canny edge", imgCanny);
	//imshow("Dilate", imgDil);

	waitKey(0);

}