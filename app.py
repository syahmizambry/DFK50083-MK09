import streamlit as st

st.title("Kalkulator BMI Klinik")

# Input berat dan tinggi
berat_input = st.text_input("Berat (kg)")
tinggi_input = st.text_input("Tinggi (meter)")

# Butang Kira BMI
if st.button("Kira BMI"):

    try:
        berat = float(berat_input)
        tinggi = float(tinggi_input)

        # Pengiraan BMI
        bmi = berat / (tinggi * tinggi)

    except ValueError:
        st.error("Sila masukkan nombor yang sah.")

    except ZeroDivisionError:
        st.error("Tinggi tidak boleh 0.")

    except Exception:
        st.error("Ralat tidak dijangka berlaku.")

    else:
        st.success(f"BMI anda ialah: {bmi:.2f}")

    finally:
        st.info("Sistem selesai memproses permintaan anda.")


# Papar rekod lama
st.subheader("Rekod Pesakit")

if st.button("Papar Rekod Lama"):

    try:
        with open("rekod_pesakit.txt", "r") as fail:
            rekod = fail.read()

        st.text(rekod)

    except FileNotFoundError:
        st.warning("Fail rekod belum diwujudkan")