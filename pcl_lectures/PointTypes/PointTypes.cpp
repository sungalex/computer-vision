#include <iostream>
#include <pcl/point_types.h>
#include <pcl/point_cloud.h>
#include <pcl/io/ply_io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <boost/thread/thread.hpp>

void main()
{
	pcl::PointXYZ p(0,0,0);
	p.x = 1; p.y = 1; p.z = 1;

	pcl::PointXYZRGB q;
	q.x = 1; q.y = 1; q.z = 1;
	q.r = 255; q.g = 255; q.b = 255;

	pcl::PointXYZRGBNormal r;
	r.x = 1; r.y = 1; r.z = 1;
	r.r = 255; r.g = 255; r.b = 255;
	r.normal_x = 1;
	r.normal_y = 1;
	r.normal_z = 1;

	pcl::visualization::PCLVisualizer viewer( "viewer" );
	HWND hwnd = FindWindow( NULL, L"viewer" );
	ShowWindow( hwnd, SW_MAXIMIZE );
	viewer.addCoordinateSystem( 1 );

	viewer.addSphere( p, 0.04, 0, 255, 0, "sphere" );

	while( ! viewer.wasStopped() )
	{
		viewer.spinOnce( 100 );
		boost::this_thread::sleep( boost::posix_time::microseconds ( 100000 ) );
		if( GetAsyncKeyState( VK_SPACE  ) ) break;
	}

	viewer.removeAllShapes();

	for( int i = 0; i < 4; ++i )
		for( int j = 0; j < 4; ++j )
			for( int k = 0; k < 4; ++k )
				viewer.addSphere( pcl::PointXYZ(i, j, k), 0.04, 0, 255, 0,
					"sphere"+std::to_string(i*100+j*10+k) );

	for( int i = 0; i < 4; ++i )
	{
		for( int j = 0; j < 4; ++j )
		{
			for( int k = 0; k < 4; ++k )
			{
				if( i < 3 )
				{
					std::string id = "linex"+std::to_string(i*100+j*10+k);
					viewer.addLine( pcl::PointXYZ(i, j, k), pcl::PointXYZ(i+1, j, k), 255, 0, 0, id );
					viewer.setShapeRenderingProperties( pcl::visualization::PCL_VISUALIZER_LINE_WIDTH, 2, id );
				}
				if( j < 3 )
				{
					std::string id = "liney"+std::to_string(i*100+j*10+k);
					viewer.addLine( pcl::PointXYZ(i, j, k), pcl::PointXYZ(i, j+1, k), 255, 0, 0, id );
					viewer.setShapeRenderingProperties( pcl::visualization::PCL_VISUALIZER_LINE_WIDTH, 2, id );
				}
				if( k < 3 )
				{
					std::string id = "linez"+std::to_string(i*100+j*10+k);
					viewer.addLine( pcl::PointXYZ(i, j, k), pcl::PointXYZ(i, j, k+1), 255, 0, 0, id );
					viewer.setShapeRenderingProperties( pcl::visualization::PCL_VISUALIZER_LINE_WIDTH, 2, id );
				}
			}
		}
	}

	viewer.resetCamera();

	while( ! viewer.wasStopped() )
	{
		viewer.spinOnce( 100 );
		boost::this_thread::sleep( boost::posix_time::microseconds ( 100000 ) );
		if( GetAsyncKeyState( VK_SPACE  ) ) break;
	}

	viewer.removeAllShapes();
}