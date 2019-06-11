#include <iostream>
#include <pcl/point_types.h>
#include <pcl/point_cloud.h>
#include <pcl/io/ply_io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <boost/thread/thread.hpp>

void main()
{
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_ptr( new pcl::PointCloud<pcl::PointXYZRGB> );
	pcl::PointCloud<pcl::PointXYZRGB> &cloud = *cloud_ptr;

	pcl::PointXYZRGB p0(255, 0, 0);
	p0.x = 10;
	p0.y = 0;
	p0.z = 0;

	pcl::PointXYZRGB p1(0, 255, 0);
	p1.x = 0;
	p1.y = 10;
	p1.z = 0;

	pcl::PointXYZRGB p2(0, 0, 255);
	p2.x = 0;
	p2.y = 0;
	p2.z = 10;

	cloud.push_back( p0 );
	cloud.push_back( p1 );
	cloud.push_back( p2 );
	std::cout << cloud[0] << '\n';
	std::cout << cloud[1] << '\n';
	std::cout << cloud[2] << '\n';

	pcl::visualization::PCLVisualizer viewer( "viewer" );
	HWND hwnd = FindWindow( NULL, L"viewer" );
	ShowWindow( hwnd, SW_MAXIMIZE );
	viewer.addCoordinateSystem( 1 );

	pcl::visualization::PointCloudColorHandlerRGBField<pcl::PointXYZRGB> rgb( cloud_ptr );
	viewer.addPointCloud<pcl::PointXYZRGB>( cloud_ptr, rgb, "cloud" );
	viewer.setPointCloudRenderingProperties( pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 10, "cloud" );

	while( ! viewer.wasStopped() )
	{
		viewer.spinOnce( 100 );
		boost::this_thread::sleep( boost::posix_time::microseconds ( 100000 ) );
		if( GetAsyncKeyState( VK_SPACE  ) ) break;
	}

	viewer.removeAllPointClouds();

	cloud.clear();
	cloud.reserve(4*4*4);

	for( int i = 0; i < 4; ++i )
	{
		for( int j = 0; j < 4; ++j )
		{
			for( int k = 0; k < 4; ++k )
			{
				pcl::PointXYZRGB p(255, 0, 0);
				p.x = i;
				p.y = j;
				p.z = k;
				cloud.push_back(p);
			}
		}
	}

	viewer.addPointCloud<pcl::PointXYZRGB>( cloud_ptr, rgb, "cloud" );
	viewer.setPointCloudRenderingProperties( pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 10, "cloud" );
	viewer.resetCamera();

	while( ! viewer.wasStopped() )
	{
		viewer.spinOnce( 100 );
		boost::this_thread::sleep( boost::posix_time::microseconds ( 100000 ) );
		if( GetAsyncKeyState( VK_SPACE  ) ) break;
	}
}