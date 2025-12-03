"""
Direct testing script for weather MCP server functions.
This allows testing without Claude Desktop or MCP client.
"""
import asyncio
from weather import get_alerts, get_forecast


async def test_get_alerts():
    """Test the get_alerts function directly."""
    print("=" * 60)
    print("Testing get_alerts(state='KY')")
    print("(Kentucky - where Highland Heights is located)")
    print("=" * 60)
    
    result = await get_alerts("KY")
    print(result)
    print()


async def test_get_forecast():
    """Test the get_forecast function directly."""
    print("=" * 60)
    print("Testing get_forecast(latitude=39.0331, longitude=-84.4519)")
    print("(Highland Heights, KY coordinates)")
    print("=" * 60)
    
    result = await get_forecast(39.0331, -84.4519)
    print(result)
    print()


async def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("WEATHER MCP SERVER - DIRECT FUNCTION TESTS")
    print("=" * 60 + "\n")
    
    try:
        await test_get_alerts()
        await test_get_forecast()
        
        print("=" * 60)
        print("All tests completed!")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

