from poc import create_application


def main():
    app = create_application()
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    main()
