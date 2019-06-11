#include <iostream>
#include <pcl/point_types.h>
#include <pcl/point_cloud.h>
#include <pcl/io/ply_io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <boost/thread/thread.hpp>

void main()
{
	std::string scan_file = "footR.ply";
	pcl::PolygonMesh mesh;
	pcl::io::loadPLYFile(scan_file, mesh);

	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_ptr( new pcl::PointCloud<pcl::PointXYZRGB> );
	pcl::fromPCLPointCloud2( mesh.cloud, *cloud_ptr );
	pcl::PointCloud<pcl::PointXYZRGB> &cloud = *cloud_ptr;

	pcl::visualization::PCLVisualizer viewer( "viewer" );
	HWND hwnd = FindWindow( NULL, L"viewer" );
	ShowWindow( hwnd, SW_MAXIMIZE );
	viewer.addCoordinateSystem( 50 );

	pcl::visualization::PointCloudColorHandlerRGBField<pcl::PointXYZRGB> rgb( cloud_ptr );
	viewer.addPointCloud<pcl::PointXYZRGB>( cloud_ptr, rgb, "cloud" );
	viewer.setPointCloudRenderingProperties( pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 3, "cloud" );

	while( ! viewer.wasStopped() )
	{
		viewer.spinOnce( 100 );
		boost::this_thread::sleep( boost::posix_time::microseconds ( 100000 ) );
		if( GetAsyncKeyState( VK_SPACE  ) ) break;
	}

	viewer.removeAllPointClouds();

	viewer.addLine( pcl::PointXYZ(100,100,0), pcl::PointXYZ(100,100,100), 255, 0, 0,  "line" );
	viewer.setShapeRenderingProperties( pcl::visualization::PCL_VISUALIZER_LINE_WIDTH, 10, "line" );
	viewer.addSphere( pcl::PointXYZ(100,100,100), 10, 0, 255, 0, "sphere" );
	viewer.resetCamera();

	while( ! viewer.wasStopped() )
	{
		viewer.spinOnce( 100 );
		boost::this_thread::sleep( boost::posix_time::microseconds ( 100000 ) );
		if( GetAsyncKeyState( VK_SPACE  ) ) break;
	}

	viewer.removeAllShapes();
}