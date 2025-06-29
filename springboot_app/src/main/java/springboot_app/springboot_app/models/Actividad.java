package springboot_app.springboot_app.models;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "actividad")
public class Actividad {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "comuna_id", nullable = false)
    private Integer comunaId;

    @Column(name = "sector")
    private String sector;

    @Column(name = "nombre", nullable = false)
    private String nombre;

    @Column(name = "email", nullable = false)
    private String email;

    @Column(name = "celular")
    private String celular;

    @Column(name = "dia_hora_inicio", nullable = false)
    private LocalDateTime diaHoraInicio;

    @Column(name = "dia_hora_termino")
    private LocalDateTime diaHoraTermino;

    @Column(name = "descripcion")
    private String descripcion;

    // Relación con Nota
    @OneToMany(fetch = FetchType.LAZY, mappedBy = "actividadId", cascade = CascadeType.ALL)
    private List<Nota> notas;

    // Getters y setters
    public Integer getId() { 
        return id; 
    }

    public void setId(Integer id) { 
        this.id = id; 
    }

    public Integer getComunaId() { 
        return comunaId; 
    }

    public void setComunaId(Integer comunaId) { 
        this.comunaId = comunaId; 
    }

    public String getSector() { 
        return sector; 
    }

    public void setSector(String sector) { 
        this.sector = sector; 
    }

    public String getNombre() { 
        return nombre; 
    }

    public void setNombre(String nombre) { 
        this.nombre = nombre; 
    }

    public String getEmail() { 
        return email; 
    }

    public void setEmail(String email) { 
        this.email = email; 
    }

    public String getCelular() { 
        return celular; 
    }

    public void setCelular(String celular) { 
        this.celular = celular; 
    }

    public LocalDateTime getDiaHoraInicio() { 
        return diaHoraInicio; 
    }

    public void setDiaHoraInicio(LocalDateTime diaHoraInicio) { 
        this.diaHoraInicio = diaHoraInicio; 
    }

    public LocalDateTime getDiaHoraTermino() { 
        return diaHoraTermino; 
    }

    public void setDiaHoraTermino(LocalDateTime diaHoraTermino) { 
        this.diaHoraTermino = diaHoraTermino; 
    }

    public String getDescripcion() { 
        return descripcion; 
    }

    public void setDescripcion(String descripcion) { 
        this.descripcion = descripcion; 
    }

    public List<Nota> getNotas() { 
        return notas; 
    }

    public void setNotas(List<Nota> notas) { 
        this.notas = notas; 
    }

    // Método para obtener el promedio de notas (??????)
    @Transient
    public String getPromedioNotas() {
        if (notas == null || notas.isEmpty()) return "-";
        double promedio = notas.stream().mapToInt(Nota::getNota).average().orElse(0.0);
        return String.format("%.2f", promedio);
    }
}