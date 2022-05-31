from ctypes import cdll
from ctypes.util import find_library


_lib = cdll.LoadLibrary(find_library("libopenslide-0.dll"))
import openslide
import argparse


def wsi_region(input_file, output_file, level, x_location , y_location, width, height):
    print("wsi_region")
    actual_slide = openslide.OpenSlide(input_file)
    img = actual_slide.read_region((x_location, y_location), level, (width, height))
    img.save(output_file)
    return img

def wsi_thumbnail(input_file, output_file, width, height):
    print("thumbnail")
    actual_slide = openslide.OpenSlide(input_file)
    img = actual_slide.get_thumbnail((width, height))
    img.save(output_file)
    return img

def wsi_label(input_file, output_file,):
    actual_slide = openslide.OpenSlide(input_file)
    label = actual_slide.associated_images["label"]
    label.save(output_file)
    print("wsi_label")
    return label

def wsi_tool():
    print("wsi:tool")



if __name__ != '__wsi_tool__':
    parser = argparse.ArgumentParser(description="WSI - CLI - method ")
    parser.add_argument("choose_func", help="'REGION' or 'THUMBNAIL' or 'LABEL', whatever you like to do... \n "
                                            "for example: wsi_tool.py THUMBNAIL ./wsi_images/CMU-1-Small-Region.tiff ./wsi_images/CMU-1-Small-Region_Thumbnail.png --width 1200 --height 1200"
                                            "or"
                                            "wsi_tool.py region ./wsi_images/CMU-1-Small-Region.tiff ./wsi_images/CMU-1-Small-Region_region.png --width 1200 --height 1200 --x 1100 --y 2000 --level 0")
    parser.add_argument("input_file", help="insert location of picture")
    parser.add_argument("output_file", help="insert location to save picture")
    parser.add_argument("--level", type=int,
                        help="scope-level between 0 and 2, necessary for Region_Func")  # "--" = optional arguments
    parser.add_argument("--x", type=int, help="x-location to start, necessary for Region_Func")
    parser.add_argument("--y", type=int, help="y-location to start, necessary for Region_Func")
    parser.add_argument("--width", type=int, help="num of width pixels for result, necessary for Region_Func and THUMBNAIL_Func")
    parser.add_argument("--height", type=int, help="num of height pixels for result, necessary for Region_Func")
    args = parser.parse_args()

    if args.choose_func.lower() == "region":
        region = wsi_region(args.input_file, args.output_file, args.level, args.x, args.y, args.width, args.height)
        print(region)
    elif args.choose_func.lower() == "thumbnail":
        thumbn = wsi_thumbnail(args.input_file, args.output_file, args.width, args.height)
        print(thumbn)
    elif args.choose_func.lower() == "label":
        label = wsi_label(args.input_file, args.output_file)
        print(label)
    else:
        print("no possible func found")



