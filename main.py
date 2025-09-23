from dotenv import load_dotenv
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv()
endpoint = os.getenv("VISION_ENDPOINT")
key=os.getenv("VISION_KEY")

try:
    endpoint = os.getenv("VISION_ENDPOINT")
    key = os.getenv("VISION_KEY")
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

# Create an Image Analysis client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Get a caption for the image. This will be a synchronously (blocking) call.
result = client.analyze_from_url(
    # image_url="https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png",
    image_url="https://firebasestorage.googleapis.com/v0/b/nyansapo-ai-v2.firebasestorage.app/o/Nyansapo_Teaching_Numeracy_Assessment_Images%2Fimage_answer_4ccd1f89-1938-465e-bcaf-a71cbdc9b142_2rSCTDY7cJZ9fWZNMFuq_2_12_ADDITION_31_43.wav?alt=media&token=24012509-3352-4606-8052-9391e938707f",
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True,  # Optional (default is False)
)

print("Image analysis results:")
# Print caption results to the console
print(" Caption:")
if result.caption is not None:
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

# Print text (OCR) analysis results to the console
print(" Read:")
if result.read is not None:
    for line in result.read.blocks[0].lines:
        print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
        for word in line.words:
            print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")